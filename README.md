# Programming Learning

Programming coursework, independent study, and algorithm practice by [Zhenjia Pan](https://github.com/zhenjiapan), an undergraduate at The Chinese University of Hong Kong, Shenzhen.

This repository records my progress in Python and C++ programming, computational thinking, and algorithmic problem-solving. It is a learning archive; implementations may be revised as my understanding develops.

## Contents

| Directory | Description |
| --- | --- |
| [MIT](MIT/) | Python and C++ coursework from MIT OpenCourseWare, including 6.096 (Introduction to C++) |
| [CUHK-SZ](CUHK-SZ/) | Programming exercises from my university courses |
| [LeetCode](LeetCode/) | Algorithm practice and solution revisions |

## Learning Goals

- Write clear, correct programs in Python and C++.
- Develop computational thinking and algorithm design skills.
- Understand data structures and time and space complexity.
- Build foundations for further study in machine learning and mathematical optimization.

## Running the Code

### Python

Use Python 3. Run standalone scripts from the directory expected by the exercise, for example:

```bash
cd CUHK-SZ/AIE1001
python3 HW260101.py
```

Some scripts require standard input, companion data files, or course-provided starter code. LeetCode submissions may require the platform's execution environment. Dependencies and execution requirements vary by exercise; this repository is not a single installable application.

### C++

For a standalone C++ exercise, open its directory and compile and run it with Clang. For example, from the repository root:

```bash
cd MIT/6.096
clang++ -std=c++17 main.cpp -o main && ./main
```

For exercises with multiple source files, follow the exercise’s build instructions.

## Notes

Solutions reflect my learning at the time of writing and may not be optimal. Course materials, starter code, and problem statements remain attributable to their respective authors. Public sharing of coursework should follow the applicable course policies. This repository is not affiliated with MIT, CUHK-Shenzhen, or LeetCode.
