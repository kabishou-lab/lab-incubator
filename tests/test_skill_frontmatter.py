"""Fail if any skill is missing SKILL.md name/description frontmatter."""

from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    data: dict[str, str] = {}
    for line in parts[1].strip().splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


class TestSkillFrontmatter(unittest.TestCase):
    def test_skills_dir_exists(self) -> None:
        self.assertTrue(SKILLS.is_dir(), f"missing {SKILLS}")

    def test_at_least_one_skill(self) -> None:
        dirs = [p for p in SKILLS.iterdir() if p.is_dir() and not p.name.startswith(".")]
        self.assertTrue(dirs, "skills/ has no skill directories")

    def test_each_skill_has_name_and_description(self) -> None:
        dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir() and not p.name.startswith("."))
        self.assertTrue(dirs, "skills/ has no skill directories")
        for skill_dir in dirs:
            path = skill_dir / "SKILL.md"
            with self.subTest(skill=skill_dir.name):
                self.assertTrue(path.is_file(), f"missing {path}")
                meta = parse_frontmatter(path.read_text(encoding="utf-8"))
                self.assertTrue(meta.get("name"), f"{path} missing name")
                self.assertTrue(meta.get("description"), f"{path} missing description")
                self.assertEqual(
                    meta["name"],
                    skill_dir.name,
                    f"{path} name={meta['name']!r} != directory {skill_dir.name!r}",
                )


if __name__ == "__main__":
    unittest.main()
