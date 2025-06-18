# General guidelines

* No communication whatsoever is allowed.
* 모든 형태의 의사소통이 금지되어 있습니다.

* This is an exam, you don't have a right to chat, listen to music, make noise, or generally do anything that may disturb the other students in any way.
* 지금은 exam세션입니다. 잡담, 음악, 소음 등 다른 학생에게 방해가 되는 행위는 모두 금지되어 있습니다.

* Your phones and other technological devices must be turned off and put away. If a phone rings, the whole row will be disqualified from the exam and kicked out immediately.
* 휴대전화 및 모든 전자기기는 전원을 꺼둔 상태로 가방, 혹은 스태프에게 맡기셔야 합니다. 만약 전자기기가 울린다면, 그 줄에 있는 모든 학생들의 시험은 0점 처리되며 모두 퇴장입니다.

* Your home directory contains three directories : "rendu", "subjects" and "traces".
* home 디렉터리에는 "rendu", "subjects", "traces", 총 3개의 디렉터리가 있습니다.

* The "subjects" directory will contain the subjects of your assignments
* "subjects" 디렉터리에는 과제들이 들어있습니다.

* The "rendu" folder is a clone of your Git turn-in repository. You will work in it, and use it as any regular Git repository.
* "rendu" 폴더는 본인이 제출해야 하는 Git 저장소의 clone 입니다. 이 안에 과제를 저장하면 되고, 일반 Git 저장소처럼 사용하면 됩니다.

* The system will not grade anything that is not pushed on your Git turn-in repository, and at the right place. Pay attention to where examshell tells you to put your files.
* 채점시스템은 알맞는 Git 저장소, 알맞는 디렉터리에 저장되어있는 파일만 채점합니다. examshell이 어디에 파일을 저장하라고 알려주는지 자세히 보십시오.

* You can only run your programs in the "rendu" directory or one of its subdirectories.
* 작성한 프로그램은 "rendu" 디렉터리 혹은 그 서브디렉터리에서만 실행할 수 있습니다. 

* You may need to read the man to carry out some assignments...
* 몇몇 과제는 man을 읽어봐야 할 수도 있습니다... 

* You will be graded by a program. You must respect the specified file/path/function names to the letter.
* 채점은 프로그램이 실행합니다. 반드시 명시되어있는 /파일/경로/함수이름을 따라야 합니다.

* Assignments will always specify which files will be collected :
* 과제는 항상 어떤 파일을 제출 해야하는지 명시합니다.
  * When an assignment asks for specific files, they will be explicitly named. For example "file1.c file1.h".
  * 과제가 특정 파일을 요구한다면 그 파일명은 과제가 요구하는 이름과 완전히 동일해야합니다. 예) "file1.c file1.h"
  * Otherwise, when filenames and/or the number of files is up to you, the assignment will say something along the lines of "*.c *.h".
  * 파일명 혹은 파일 개수가 정해져 있지 않으면, "*.c *.h"의 형식으로 쓰여있을 것입니다.
  * When a Makefile is required, it will ALWAYS be explicitly stated.
  * Makefile이 필요한 과제는 언제나 구체적으로 명시되어있습니다.

* In case of technical problem, question about the subject, or any other problem, you must get up silently and wait for a member of the staff to come to you. It is forbidden to ask your neighbors, or to verbally call for a staff member.
* 기술적인 문제, 과제에 대한 질문 외에 모든 문의를 위해서는 조용히 일어나 스태프가 직접올때까지 기다려야합니다. 주변동료에게 질문, 스태프를 구두로 부르는 것은 금지 되어 있습니다.

* Any equipment not explicitly allowed is implicitly forbidden.
* 사용이 가능하다고 명시적으로 언급되지 않은 물품은 금지되어 있습니다.

* Any exit is definitive, you can not come in again.
* 한번 실험공간을 나가면 다시 돌아올 수 없습니다.

* Staff members may kick you out of the exam without warning if they deem it necessary.
* 스태프가 필요하다고 판단되면 예고 없이 시험에서 퇴장시킬 수 있습니다.

* You are allowed blank pieces of paper, and a pen. No notebooks, notes, or any help of the sort. You are alone to face this exam.
* 빈 종이, 펜만 허용됩니다. 공책, 노트, 어떤 형식의 도움도 금지되어 있습니다. 혼자의 힘으로 시험에 맞서십시오.

# Coding guidelines

* You must write your code in pure c only.
* code는 순수한 c로만 써야 합니다.

* Useful functions and files will sometimes be given to you in the subject directory
* 가끔씩 유용한 함수 혹은 파일이 subject 디렉터리에 주어지기도 합니다.

* The correction is fully automated, and performed by the program we know as Deepthought.
* 채점은 완전히 자동화 되어있으며, Deepthought라는 프로그램이 수행합니다.


* When an assignment asks you to write a program with one or more explicitly named files, it will be compiled with the following command: clang -Wall -Wextra -Werror file1.c file2.c file3.c -o program_name.
* 과제가 프로그램 작성에 필요한 파일의 이름을 명시한다면, 그 프로그램은 다음과 같이 컴파일이 됩니다. clang -Wall -Wextra -Werror file1.c file2.c file3.c -o program_name.

* When the assignment leaves the filenames up to you, it will be compiled with: clang -Wall -Wextra -Werror *.c -o program_name.
* 과제가 파일명을 명시 하지 않는다면 다음과 같이 컴파일 됩니다. clang -Wall -Wextra -Werror *.c -o program_name.

* Finally, when you must only turn in a function (so, one file), it will be compiled with clang -c -Wall -Wextra -Werror yourfile.c, then we will compile our main function and link them together to create a test program.
* 마지막으로, 함수만을 제출한다면, 다음과 같이 컴파일됩니다. clang -c -Wall -Wextra -Werror yourfile.c. 그리고 그 오브젝트 파일은 deeptought의 자체 main 함수와 링크되어 테스트 프로그램이 생성됩니다.

* Allowed functions will be specified in the headers of the assignments.  You may recode any other function you think is necessary. Using a function that's not explicitly allowed is considered cheating, and will result in a failing grade, with no possible discussion or appeal whatsoever.  You've been warned.
* 허용된 함수는 과제의 헤더에 명시되어 있습니다. 필요하다고 생각되는 함수는 재구현 할 수 있습니다. 허용된다고 명시되지 않은 함수를 쓰는 것은 부정행위로 간주, 낙제점이 부여되며, 어떠한 합의도 없습니다.

* Any function that isn't explicitly allowed is implicitly forbidden.
* 명시적으로 허용되지 않은 함수는 사용이 금지되어 있습니다.
