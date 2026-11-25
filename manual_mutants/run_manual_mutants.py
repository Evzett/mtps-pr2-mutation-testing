"""Прогон набора тестов против ручных мутантов.

Для каждого мутанта создаётся временная копия проекта, в которой
src/email_validator.py заменяется кодом мутанта, после чего запускается pytest.
Ненулевой код возврата pytest означает, что мутант убит.

Запуск из корня проекта:
    python manual_mutants/run_manual_mutants.py [путь_к_файлу_тестов]
"""
import pathlib
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
MUTANTS = sorted((ROOT / "manual_mutants").glob("m*_*.py"))


def run_against(mutant: pathlib.Path, tests_file: pathlib.Path) -> bool:
    """Возвращает True, если мутант убит."""
    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)
        shutil.copytree(ROOT / "src", tmp / "src")
        (tmp / "tests").mkdir()
        (tmp / "tests" / "__init__.py").write_text("")
        shutil.copy(tests_file, tmp / "tests" / "test_email_validator.py")
        shutil.copy(mutant, tmp / "src" / "email_validator.py")
        proc = subprocess.run(
            [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "tests"],
            cwd=tmp, capture_output=True, text=True,
        )
        return proc.returncode != 0


def main() -> int:
    tests_file = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "tests" / "test_email_validator.py"
    print(f"Набор тестов: {tests_file.name}")
    killed = 0
    for m in MUTANTS:
        is_killed = run_against(m, tests_file)
        killed += is_killed
        print(f"  {m.name:<28} {'KILLED' if is_killed else 'SURVIVED'}")
    print(f"Убито {killed} из {len(MUTANTS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
