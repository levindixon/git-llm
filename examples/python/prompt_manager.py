#!/usr/bin/env python3
"""
Git LLM Prompt Manager - Python implementation for managing LLM prompts with Git
"""

import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Union
import argparse
import re


class GitLLMPromptManager:
    """Manage LLM prompts in Git repositories"""
    
    def __init__(self, repo_path: Path = Path.cwd()):
        self.repo_path = repo_path
        self.prompts_dir = repo_path / ".prompts"
        self.notes_ref = "refs/notes/llm-prompts"
        
    def init(self) -> None:
        """Initialize prompt tracking in the repository"""
        # Create directory structure
        (self.prompts_dir / "by-hash").mkdir(parents=True, exist_ok=True)
        (self.prompts_dir / "by-date").mkdir(parents=True, exist_ok=True)
        
        # Create config file
        config = {
            "version": "1.0",
            "created": datetime.utcnow().isoformat() + "Z",
            "storage": {
                "use_trailers": True,
                "use_notes": True,
                "use_directory": True
            }
        }
        
        with open(self.prompts_dir / "config.json", "w") as f:
            json.dump(config, f, indent=2)
            
        # Create .gitignore
        gitignore_content = """*.tmp
*.bak
pending-*.json
.current-llm-prompt
.current-llm-model
"""
        with open(self.prompts_dir / ".gitignore", "w") as f:
            f.write(gitignore_content)
            
        print("✓ LLM prompt tracking initialized")
        
    def add_prompt(self, prompt: str, model: str = "unknown") -> None:
        """Add a prompt for the next commit"""
        if not prompt:
            raise ValueError("Prompt cannot be empty")
            
        # Save prompt for git hooks
        with open(self.repo_path / ".current-llm-prompt", "w") as f:
            f.write(prompt)
            
        with open(self.repo_path / ".current-llm-model", "w") as f:
            f.write(model)
            
        print(f"✓ Prompt saved for next commit")
        print(f"Model: {model}")
        print(f"Prompt: {prompt}")
        
    def get_prompt(self, commit: str = "HEAD") -> Optional[Dict[str, str]]:
        """Get prompt for a specific commit"""
        # Get commit hash
        try:
            commit_hash = subprocess.check_output(
                ["git", "rev-parse", commit],
                cwd=self.repo_path,
                text=True
            ).strip()
        except subprocess.CalledProcessError:
            raise ValueError(f"Invalid commit reference: {commit}")
            
        prompt_data = {}
        
        # Try to get from commit trailers
        try:
            trailers = subprocess.check_output(
                ["git", "log", "-1", "--format=%(trailers)", commit_hash],
                cwd=self.repo_path,
                text=True
            ).strip()
            
            for line in trailers.split('\n'):
                if line.startswith("LLM-Prompt:"):
                    prompt_data["prompt"] = line[11:].strip()
                elif line.startswith("LLM-Model:"):
                    prompt_data["model"] = line[10:].strip()
                elif line.startswith("LLM-Timestamp:"):
                    prompt_data["timestamp"] = line[14:].strip()
        except subprocess.CalledProcessError:
            pass
            
        # Try to get from git notes
        try:
            note = subprocess.check_output(
                ["git", "notes", "--ref", self.notes_ref, "show", commit_hash],
                cwd=self.repo_path,
                text=True,
                stderr=subprocess.DEVNULL
            ).strip()
            
            if note:
                try:
                    note_data = json.loads(note)
                    prompt_data.update(note_data)
                except json.JSONDecodeError:
                    prompt_data["note"] = note
        except subprocess.CalledProcessError:
            pass
            
        # Try to get from prompts directory
        prompt_file = self.prompts_dir / "by-hash" / f"{commit_hash[:7]}.json"
        if prompt_file.exists():
            with open(prompt_file) as f:
                file_data = json.load(f)
                prompt_data.update(file_data)
                
        return prompt_data if prompt_data else None
        
    def list_prompts(self, format: str = "text") -> Union[str, List[Dict]]:
        """List all prompts in the repository"""
        prompts = []
        
        # Get all commits with LLM-Prompt trailers
        try:
            log_output = subprocess.check_output(
                ["git", "log", "--format=%H|%s|%aI|%(trailers:key=LLM-Prompt,valueonly)"],
                cwd=self.repo_path,
                text=True
            ).strip()
            
            for line in log_output.split('\n'):
                if line:
                    parts = line.split('|', 3)
                    if len(parts) >= 4 and parts[3]:
                        prompts.append({
                            "commit": parts[0],
                            "subject": parts[1],
                            "date": parts[2],
                            "prompt": parts[3]
                        })
        except subprocess.CalledProcessError:
            pass
            
        if format == "json":
            return prompts
        else:
            # Text format
            output = ["LLM Prompts in Repository:", ""]
            for p in prompts:
                output.append(f"Commit: {p['commit'][:7]} {p['subject']}")
                output.append(f"  Date: {p['date']}")
                output.append(f"  Prompt: {p['prompt']}")
                output.append("")
            return '\n'.join(output)
            
    def search_prompts(self, pattern: str) -> List[Dict]:
        """Search for prompts matching a pattern"""
        results = []
        
        # Search in commit messages
        try:
            grep_output = subprocess.check_output(
                ["git", "log", "--grep", f"LLM-Prompt:.*{pattern}", "--format=%H"],
                cwd=self.repo_path,
                text=True,
                stderr=subprocess.DEVNULL
            ).strip()
            
            for commit_hash in grep_output.split('\n'):
                if commit_hash:
                    prompt_data = self.get_prompt(commit_hash)
                    if prompt_data:
                        prompt_data["commit"] = commit_hash
                        results.append(prompt_data)
        except subprocess.CalledProcessError:
            pass
            
        # Search in prompt files
        if self.prompts_dir.exists():
            for prompt_file in (self.prompts_dir / "by-hash").glob("*.json"):
                try:
                    with open(prompt_file) as f:
                        data = json.load(f)
                        if pattern.lower() in json.dumps(data).lower():
                            results.append(data)
                except (json.JSONDecodeError, IOError):
                    pass
                    
        return results
        
    def export_prompts(self, output_file: Path) -> None:
        """Export all prompts to a file"""
        export_data = {
            "export_date": datetime.utcnow().isoformat() + "Z",
            "repository": self._get_repo_url(),
            "prompts": self.list_prompts(format="json")
        }
        
        with open(output_file, "w") as f:
            json.dump(export_data, f, indent=2)
            
        print(f"✓ Exported {len(export_data['prompts'])} prompts to {output_file}")
        
    def _get_repo_url(self) -> str:
        """Get the repository URL"""
        try:
            return subprocess.check_output(
                ["git", "config", "--get", "remote.origin.url"],
                cwd=self.repo_path,
                text=True
            ).strip()
        except subprocess.CalledProcessError:
            return "local"
            
    def add_note_to_commit(self, commit: str, prompt_data: Dict) -> None:
        """Add a note with prompt data to a commit"""
        note_content = json.dumps(prompt_data, indent=2)
        
        subprocess.run(
            ["git", "notes", "--ref", self.notes_ref, "add", "-m", note_content, commit],
            cwd=self.repo_path,
            check=True
        )
        
        print(f"✓ Added prompt note to commit {commit}")
        
    def create_prompt_file(self, commit_hash: str, prompt_data: Dict) -> None:
        """Create a prompt file in the .prompts directory"""
        # Create date-based directory
        date = datetime.fromisoformat(prompt_data.get("timestamp", datetime.utcnow().isoformat()))
        date_dir = self.prompts_dir / "by-date" / f"{date.year:04d}" / f"{date.month:02d}" / f"{date.day:02d}"
        date_dir.mkdir(parents=True, exist_ok=True)
        
        # Save by hash
        hash_file = self.prompts_dir / "by-hash" / f"{commit_hash[:7]}.json"
        with open(hash_file, "w") as f:
            json.dump(prompt_data, f, indent=2)
            
        # Save by date
        date_file = date_dir / f"{date.strftime('%H-%M-%S')}-{commit_hash[:7]}.json"
        with open(date_file, "w") as f:
            json.dump(prompt_data, f, indent=2)


def main():
    """CLI interface for the prompt manager"""
    parser = argparse.ArgumentParser(
        description="Manage LLM prompts in Git repositories",
        prog="git-llm"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # Init command
    subparsers.add_parser("init", help="Initialize prompt tracking")
    
    # Add command
    add_parser = subparsers.add_parser("add", help="Add prompt for next commit")
    add_parser.add_argument("prompt", help="The prompt text")
    add_parser.add_argument("-m", "--model", default="unknown", help="LLM model name")
    
    # Show command
    show_parser = subparsers.add_parser("show", help="Show prompt for a commit")
    show_parser.add_argument("commit", nargs="?", default="HEAD", help="Commit reference")
    
    # List command
    list_parser = subparsers.add_parser("list", help="List all prompts")
    list_parser.add_argument("-f", "--format", choices=["text", "json"], default="text", help="Output format")
    
    # Search command
    search_parser = subparsers.add_parser("search", help="Search prompts")
    search_parser.add_argument("pattern", help="Search pattern")
    
    # Export command
    export_parser = subparsers.add_parser("export", help="Export all prompts")
    export_parser.add_argument("-o", "--output", default="prompts-export.json", help="Output file")
    
    args = parser.parse_args()
    
    # Create manager instance
    manager = GitLLMPromptManager()
    
    # Execute command
    try:
        if args.command == "init":
            manager.init()
        elif args.command == "add":
            manager.add_prompt(args.prompt, args.model)
        elif args.command == "show":
            prompt_data = manager.get_prompt(args.commit)
            if prompt_data:
                print(json.dumps(prompt_data, indent=2))
            else:
                print(f"No prompt found for commit {args.commit}")
        elif args.command == "list":
            result = manager.list_prompts(args.format)
            if args.format == "json":
                print(json.dumps(result, indent=2))
            else:
                print(result)
        elif args.command == "search":
            results = manager.search_prompts(args.pattern)
            print(json.dumps(results, indent=2))
        elif args.command == "export":
            manager.export_prompts(Path(args.output))
        else:
            parser.print_help()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()