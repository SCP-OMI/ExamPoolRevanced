import os
import difflib
import argparse

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

REQUIRED_FILES = [
    "{name}.c",
    "generator.py",
    "main.c",
    "profile.yml"
]

def check_subject(subject_folder, subjects_path, corrections_path):
    subject_dir = os.path.join(subjects_path, subject_folder)
    correction_dir = os.path.join(corrections_path, subject_folder)

    output_lines = [f"\n📁 Checking subject: {subject_folder}"]
    terminal_lines = [f"\n{CYAN}📁 Checking subject: {subject_folder}{RESET}"]

    # Check for subject.en.txt
    subject_file = os.path.join(subject_dir, "subject.en.txt")
    if os.path.isfile(subject_file):
        output_lines.append("✅ subject.en.txt found.")
        terminal_lines.append(f"{GREEN}✅ subject.en.txt found.{RESET}")

        with open(subject_file, "r", encoding="utf-8") as f:
            content = f.read()
            lines = content.splitlines()

        # --- Assignment name check ---
        assignment_line = next((line for line in lines if "Assignment name  : " in line), None)
        if assignment_line:
            assigned_name = assignment_line.split("Assignment name  : ")[1].strip()
            if assigned_name == subject_folder:
                output_lines.append("✅ Assignment name matches folder.")
                terminal_lines.append(f"{GREEN}✅ Assignment name matches folder.{RESET}")
            else:
                output_lines.append(f"❌ Assignment name mismatch: found '{assigned_name}', expected '{subject_folder}'")
                terminal_lines.append(f"{RED}❌ Assignment name mismatch: found '{assigned_name}', expected '{subject_folder}'{RESET}")
        else:
            output_lines.append("❌ No 'Assignment name:' line found.")
            terminal_lines.append(f"{RED}❌ No 'Assignment name:' line found.{RESET}")

        # --- Example check ---
        lower_lines = [line.lower() for line in lines]
        if "example" in " ".join(lower_lines):
            example_idx = next((i for i, line in enumerate(lower_lines) if "example" in line), -1)
            after_example = lines[example_idx + 1:] if example_idx + 1 < len(lines) else []
            has_example_content = any(line.strip() for line in after_example)
            if has_example_content:
                output_lines.append("✅ Example content found after 'Example'.")
                terminal_lines.append(f"{GREEN}✅ Example content found after 'Example'.{RESET}")
            else:
                output_lines.append("❌ 'Example' found but no content after it.")
                terminal_lines.append(f"{RED}❌ 'Example' found but no content after it.{RESET}")
        else:
            output_lines.append("❌ No 'Example' section found.")
            terminal_lines.append(f"{RED}❌ No 'Example' section found.{RESET}")
    else:
        output_lines.append("❌ subject.en.txt is missing.")
        terminal_lines.append(f"{RED}❌ subject.en.txt is missing.{RESET}")

    # Check corrections folder
    if not os.path.isdir(correction_dir):
        output_lines.append("❌ Correction folder is missing.")
        terminal_lines.append(f"{RED}❌ Correction folder is missing.{RESET}")
        return output_lines, terminal_lines

    actual_files = os.listdir(correction_dir)
    expected_set = set()

    # Check required files
    for pattern in REQUIRED_FILES:
        expected_name = pattern.format(name=subject_folder)
        expected_set.add(expected_name)

        if expected_name in actual_files:
            output_lines.append(f"✅ {expected_name} found.")
            terminal_lines.append(f"{GREEN}✅ {expected_name} found.{RESET}")
        else:
            output_lines.append(f"❌ {expected_name} is missing.")
            terminal_lines.append(f"{RED}❌ {expected_name} is missing.{RESET}")
            close_matches = difflib.get_close_matches(expected_name, actual_files, n=1, cutoff=0.7)
            if close_matches:
                suggestion = f"   ⚠️ Possible typo: {close_matches[0]} (expected: {expected_name})"
                output_lines.append(suggestion)
                terminal_lines.append(f"{YELLOW}{suggestion}{RESET}")

    # Warn about extra files
    extras = [f for f in actual_files if f not in expected_set]
    if extras:
        output_lines.append("⚠️ Extra or suspicious files found:")
        terminal_lines.append(f"{YELLOW}⚠️ Extra or suspicious files found:{RESET}")
        for extra in extras:
            output_lines.append(f"   - {extra}")
            terminal_lines.append(f"{YELLOW}   - {extra}{RESET}")

    return output_lines, terminal_lines


def run_check(subjects_path, corrections_path, output_file):
    all_output_lines = []
    all_terminal_lines = []

    for folder in os.listdir(subjects_path):
        subject_full_path = os.path.join(subjects_path, folder)
        if not os.path.isdir(subject_full_path):
            continue
        out_file, out_terminal = check_subject(folder, subjects_path, corrections_path)
        all_output_lines.extend(out_file)
        all_terminal_lines.extend(out_terminal)

    with open(output_file, "w") as f:
        for line in all_output_lines:
            f.write(line + "\n")

    for line in all_terminal_lines:
        print(line)

    print(f"\n{GREEN}✅ Check complete. Results saved to {output_file}{RESET}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check structure of subjects and corrections folders.")
    parser.add_argument("--subjects", required=True, help="Path to subjects folder")
    parser.add_argument("--corrections", required=True, help="Path to corrections folder")
    parser.add_argument("--output", default="check_results.txt", help="Output file name (default: check_results.txt)")
    args = parser.parse_args()

    run_check(args.subjects, args.corrections, args.output)