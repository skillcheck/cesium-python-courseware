## Introduction

This is course is intended to take you beyond the basics of Python and guide you into larger scale software development with Python. While we will quickly go over some of the basics, there are plenty of other good resources (books and online) which can teach you these so we won't repeat those. Some of the online resources include:

https://www.w3schools.com/python/
https://learnpython.com/

This course is organized into the following Lessons:

- [Getting Started](GettingStarted.md)
  Getting started with installing, setup, and testing of interpret and tools.
- [Lesson 0: The Basics](Basics.md)
  Quick overview of the fundamentals.
- [Lesson 1: Organizing into Functions and Modules](FunctionsAndModules.md)
  Initial steps into organizing more complex code.
- [Lesson 2: Non-linear Programming](Nonlinear.md)
- [Lesson 3: Organizing into Classes](Classes.md)
- [Lesson 4: User Interfaces and Event-based Programming](UIEventBased.md)
- [Lesson 5: Production and Packaging](ProductionAndPackaging.md)
- [Lesson 6: Introspection](Introspection.md)
- [Lesson 7: Application and Framework Development](ApplicationFramework.md)
- [Lesson 8: Mixing with other Languages](MixingLanguages.md)
- [Lesson 9: Network Programming](Network.md)
- [Lesson 10: Graphics Programming](Graphics.md)
- [Lesson 11: Machine Learning Programming](MachineLearning.md)


### Intended Audience

This course is intended as an accelerated introduction to programming with Python. Experienced programmers from other langues can get going quickly without too much explanation. Less experienced programmers will be guided through a natural progression of the language and programming in general and referred to other resources when more detail is necessary and is sufficiently provided elsewhere.

### How to use

As in many courses, this course is designed to progressively build up from simple to more complex examples for each successive lesson. However, instead of making separate files for each stage of progression, it relies on the facilities provided by git to step through each stage of the development process. In this way, you can see how the files change yourself using any git-compatible tools. You can of course use the git repository yourself to track your own changes to the code (which is good practice anyway).

If you don't have it already, all of the course material, including the source code and documentation (and this document) are in the github repository located here:

https://github.com/skillcheck/cesium-courseware-python

If you look at the commit history of the repository, you will see that each commit is another (incremental) step along the progression of the lesson. This gives more fine-grained increments to showing the code progression without having to make many copies of the code.

TODO: show image of history

The start of each lesson is marked by a tag, e.g. Lesson_00. As the documentation is also part of the repository, when you checkout a certain commit, you will only have the documentation up to that point. Of course you can just checkout the last commit to have the full document, and also the final result of each lesson.

To follow the course, make a branch at the commit corresponding to the lesson you want to start at, e.g:

```
> git branch mybranch Lesson_00
> git checkout mybranch
```

When you want to progress to the next step (or jump to another step in the course), you can set your branch to the corresponding commit, e.g.:

```
> git reset --hard LESSON_01
```

In gitk, right-click on the new commit, select "Reset <branch> to here", then select "Hard: Reset working tree and index (discard ALL local changes)".

**WARNING:** This will throw away any changes you have made to any of the (existing) files, so save them and possibly merge/rebase them into the repo if you don't want to lose them.

TODO: complete section

### About the Author

Chris Skluzacek studied Physics and Mathematics in college and one of his favorite courses was Computational Physics because it showed how the powerful tools of a computers and software could be used to simulate some of the things he was learning in Physics at the moment. After college he worked for a large military contractor in the US as an Operations Analyst, but switched to software development because he wanted to know how the software tools he was using worked, and how to make his own tools. Of particular interest was in the development of 3D graphics for use in visual simulation and scientific visualisation.

In 2001 he started his own small software consulting firm in the Netherlands and specialized in making visual simulation software in the Aerospace and Automotive industries. The main product he has developed is OpenIGS, a general-purpose application development framework primarily used for visual simulation integration 3D graphics, UI, Networking, with Simulation. He programs primarily in C++ for desktop OSes (Linux and Windows) but has dabbled in mobile development (Android) and other languages (Java and Python) and technologies such as VR/AR/MR, Computer Vision and Machine Learning. He has recently become more interested in Python for larger scale development which was the motivation for making this course.


### Credits

Thanks go to Anna Fogelmane for reviewing and using thise course. Our skill exchange (she giving me piano lessons) was a major motivation for making this course.

TODO: complete section

