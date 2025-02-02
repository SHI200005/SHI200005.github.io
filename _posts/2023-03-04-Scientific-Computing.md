---
layout: post
title: (En) Scientific Computing in C++ 1.0
categories: PhD-UT-Course-Review
description: 真.码农
keywords: Scientific Computing
mathjax: true
---

In this course, we compute in **C++**, a compiled language, since we need fast computing, or we cannot get our degree until death. We also use **unix-like** environment to run our jobs on **high performance clusters (HPC)**.

The content and examples come from [PHY1610 (Winter 2023)](https://education.scinet.utoronto.ca/course/view.php?id=1234#section-0), given by Professor [Ramses van Zon](https://www.scinethpc.ca/ramses-van-zon/).

The corresponding examples are in this repo [PHY1601_Winter_2023](https://github.com/SHI200005/Comp_23).

20230304 Ver0.1 20230424 Ver0.9

Everybody knows (after 2022): if you have issues with coding, ask **ChatGPT** first! It is fantastic!!!

Attention: If you are using MobaXterm to SSH to the teach cluster, when you are logging in, entering your password, you will see nothing indicating you are entering. Just enter the password and press 'enter'! Don't be stuck for two weeks wondering 'why can't I enter the password'!!!

## Software Development

### C++ introduction

C++ is a **compiled language**: files containing the basic ‘actions’ are to be compiled into a set of basic machine language instructions that the CPU can execute, which means usually we **cannot debug line by line**, unlike python and MATLAB. So, how to debug? 

- Usually we **insert some print-out lines** in our code, to monitor where it crashes. 
- If you use [Visual Studio Code](https://code.visualstudio.com), in the [C/C++ extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools), you can create "tasks.json" and "launch.json" as instructed, and then debug line by line. [example](https://github.com/SHI200005/Examples/tree/main/debug)

**State**: Program state is stored in memory. When a program ends, its state is gone. Files are a way to store data persistently, but fall under I/O (input/output).

**Scope**: If you define a variable inside a code block, it exists only until the code hits the closing curly brace (}) that correspond to the opening curly brace ({) that started the block. This is its local scope.

#### Arguments by value or by reference

1. Passing function arguments by value.

   ```
   // passval.cpp
   #include <iostream>
   void inc(int i)
   {
   	i = i+1;
   }
   
   int main()
   {
   	int j = 10;
   	inc(j);
   	std::cout << j << "\n";
   }
   ```

   Copied, and the result is 10.

2. Passing function arguments by reference.

   ```
   // passref.cpp
   #include <iostream>
   void inc(int &i)
   {
   	i = i+1;
   }
   
   int main()
   {
   	int j = 10;
   	inc(j);
   	std::cout << j << "\n";
   }
   ```

   Referred, and the result is 11.

But who will write the 'add' function like this... This is just for demonstrating... We all write and call...

```
// add.cpp
#include <iostream>
int add(int i)
{
	i = i+1;
	return i;
}

int main()
{
	int j = 10;
	j = add(j);
	std::cout << j << "\n";
}
```

#### Casting one numeric type into another

Use static_cast<OTHERTYPE>(...). But I don't. Actually, you don't need to worry about this! There is **automatic casting**! lol

#### Pointers

If you are not a professional coder, don't be afraid of pointers in C++. As a computation physicist, maybe the most important thing you need to know about pointers is **arrays** (discussed later), so that when you call an array in a function, it takes a copy of the pointer to the first element of the array, but not copying the whole array.

#### Command Line Argument

 ```
 #include <iostream>
 int main(int argc, char* argv[]) {
 	for (int i=0; i<argc; i++) {
 		std::cout << argv[i] << "\n";
 	}
 }
 ```

```
$ g++ -std=c++17 -o printargs printargs.cpp
$ ./printargs Hello There! # here are command line arguments
./printargs # Why this come out? argv is an array of character string, with the first string, argv[0] equal to the command
Hello
There!
$
```

### Modularity and Make

Don't write all lines linearly in 'int(main){}'. Try to pack the function (an activity or purpose natural to or intended for a person or thing) into a function (the coding term).

**Make** is a general framework that is used to compile code, of any type.

<img src="\images\blog\Computing_Make.JPG" alt="Computing_Make" style="zoom:80%;" />

Example: [Assignment 3: Modularize with make and git.](https://github.com/SHI200005/Comp_23/tree/main/A3_Modularize)

Unfortunately, by modularized with make, you cannot rely on the report from your Visual Studio Code anymore.

### Arrays

#### Automatic arrays (very dangerous)

Arrays like

```
int a[100000000]; # 1D array
double a[10000][10000]; #2D array
```

are automatic arrays. They are very dangerous.  C standard only says at least one automatic array of at least 65535 bytes can be used. In practice, limit is set by compiler and OS. Compiler **will not warn** about the limit; the program will **just crash**. *Believe me, this is how I was stuck in my first month of my research project... **Damn**!!!* You need to use

#### Dynamic Arrays (only 1D)

```
int* a = new[6] {2,3,4,6,8,2};
...(some code)
delete[] a; // must deallocate!
```

```
#include <memory>

std::unique_ptr<double[]> a;
a = std::make_unique<double[]>(100);
// no delete necessary
```

Actually I never use these. For multidimensional options (**also work for 1D array**), see below.

#### Libraries for multidimensional arrays

1. [rarray](https://github.com/vanzonr/rarray) by Ramses

   ```
   #include <rarray> // you need to install it first
   
   rarray<double,2> a(10,10);
   // compile with optimization (at least -O2)
   ```

2. The vector class

   ```
   # include <vector>
   
   vector<vector<double>> a (800,vector<double> (800))
   ```

### I/O

<img src="\images\blog\Computing_File.JPG" alt="Computing_Make" style="zoom:80%;" />

Two options of writing the **multidimensional array** results: write in human-readable ASCII file (what I usually do in my group, but slow and large), write in NetCDF files (you need to write codes for writing (annoying), ask ChatGPT how to write).

Example: [Assignment 5: Solve ODE and store in NetCDF file.](https://github.com/SHI200005/Comp_23/tree/main/A5_ODE_netCDF), in [mzasolve.cpp](https://github.com/SHI200005/Comp_23/blob/main/A5_ODE_netCDF/mzasolve.cpp)

## Numerical Tools

### Numeric

<img src="\images\blog\Computing_Numerics.JPG" alt="Computing_Numerics" style="zoom:80%;" />

### Using Libraries

There are lots of well-established libraries for scientific computing, such as ODEs, PDEs, FFT, etc. For example, **GNU Scientific Library ([GSL](https://www.gnu.org/software/gsl/))** is a C library containing many useful scientific routines. On teach cluster, load **gsl/2.7.1**. If you need to use them, use the library, don't code by yourself!

When you are using a library which is not C++ standard library, you should add **-l flags** and **link to the library** when compiling (see the [example Makefile](https://github.com/SHI200005/Comp_23/blob/main/A5_ODE_netCDF/Makefile)). 

### Examples

- Ordinary Differential Equations

  Example: [Assignment 5: Solve ODE and store in NetCDF file.](https://github.com/SHI200005/Comp_23/tree/main/A5_ODE_netCDF) with adaptive step-size control by **gsl**.

- Partial Differential Equations

  We can use linear algebra formulation to solve PDEs, see examples below.

- Linear Algebra

  In C++, we use **BLAS (Basic Linear Algebra Subroutines)** to solve linear algebra problems. Check [this link](https://netlib.org/blas/blast-forum/) for the routines you are looking for.

  Example: [Assignment 6: Using BLAS for the 1d wave](https://github.com/SHI200005/Comp_23/tree/main/A6_PDE_LinearAlgebra_BLAS) Attention: Here I used dense matrix, but usually it is a sparse matrix and we should use sparse matrix to interpret. However, I am a rookie who don't know how to code...

- Random numbers / Monte Carlo

  There are a lot of random pseudo number generators. When applying them, we don't know their quality. Employ two random number generators, and see if they give, statistically speaking, the same result. 

  Here is an example of generating fast random numbers uniformly distributed between 0 and 1.

  ````
  #include <random>
  
  // Set the seed value (where they start)
  const unsigned seed = 42;
  
  // Create a mt19937_64 random number generator with the seed
  std::mt19937_64 rng(seed);
  
  // Create a uniform distribution for double values in the range [0, 1]
  std::uniform_real_distribution<double> dist(0.0, 1.0);
  ````

### Fast Fourier Transforms

Example of using the **FFTW** library

```
#include <complex>
#include <rarray>
#include <fftw3.h>

typedef std::complex<double> complex;
void fft_fast(const rvector<complex>& f, rvector<complex>& fhat, bool inverse)
{
	int n = f.size();
			fftw_plan p = fftw_plan_dft_1d(n,
			(fftw_complex*)f.data(), (fftw_complex*)fhat.data(),
			inverse?FFTW_BACKWARD:FFTW_FORWARD,
	FFTW_ESTIMATE);
	fftw_execute(p);
	fftw_destroy_plan(p);
}
```

## High-Performance Computing

### Profiling Tools

From now on, we are going to log in to HPC, submit our huge computational jobs to the compute nodes, log out, so that we can watch Netflix using our own computer (kidding, I never have time to watch Netflix... So that I can read papers, write essays and go to bed...)

Before submitting our jobs, we need to give an estimate running time to the scheduler. Therefore, we need to know the time elapse of running (a small part of) the program.

In the course, we learned how to sample the lines that the program spend most time on, and then try to improve these lines. However, usually I know where the program spend most time. In practice, I only need to know the running time. Here is my own example of embedding a timer in my program.

```
#include <iostream>       // for output
#include <ctime>          // for timing functions

//defining the timer class for timing convenience
class timer
{
	clock_t start;
public:
	timer();
	~timer();
};

int main(int argc, char *argv[])
{
  //starting the timer
	timer ob;
	
	... some code

}

timer::timer(){start=clock();}
timer::~timer()
{
	int hour,min;
	float sec;
	clock_t end;
	
	end = clock();
    
	sec = (float)(end-start) / CLOCKS_PER_SEC;
	min = (int)sec / 60;
    sec = sec - 60*min;
	hour = (int)min / 60;
    min = min - 60*hour;
	
	std::cout << "Time Elapsed : " << hour << " hour: " << min << " min: " << sec << " sec. " << std::endl;
}
```

### Intro to Parallel Computing

The following three examples shows how to apply parallel programming. Before, you ssh-ed to the teach cluster and did your job on the **log in node**. The jobs usually only took no more than 2 seconds. Now you are doing larger computation, and when you apply computation in your research, you may come across some work which takes 40 hours. You may not want to monitor your computer for running 40 hours. Let's throw the tedious work on the **compute nodes** and run away! Examples of how to submit a job to the compute nodes via **SBATCH** will be included.

#### Race condition (you should avoid it)

A race condition is a common issue in parallel programming where two or more threads access a shared resource at the same time, resulting in unpredictable behavior or incorrect results.

In a race condition, the final output depends on the order in which the threads execute, and this order is non-deterministic and may vary between runs or on different hardwares. Race conditions typically arise when multiple threads try to read and write a shared variable or resource simultaneously, leading to inconsistencies or unexpected results.

#### Shared Memory Programming with OpenMP

<img src="\images\blog\Computing_Parallel.JPG" alt="Computing_Parallel" style="zoom:80%;" />

Consider: we are computing the time evolution of a 2D wave, by solving PDEs. We know that for taking one time step, the state of a grid only depend on the previous state of its adjacent grids. Naturally, we can chop the computing for grids within a time step. Example: [Assignment 8: Parallel two-dimensional wave equation.](https://github.com/SHI200005/Comp_23/tree/main/A8_Parallel_2Dwave)

#### Distributed Memory Programming with MPI

<img src="\images\blog\Computing_MPI.JPG" alt="Computing_MPI" style="zoom:80%;" />

<img src="\images\blog\Computing_MPI2.JPG" alt="Computing_MPI2" style="zoom:80%;" />

Consider: from above, we now have the time evolution of the 2D wave. In a NecCDF file, results of huge amount of grids are stored for each time step, and there are huge amount of time steps. For each time step, we want to calculate the energy of that time step, from results of all the grids. Since the number of grids is huge, we chop the huge grids (by rows), calculate the local energy, sum local energies together, and get the total energy for that time step. Then we move on to calculate the next time step. Why we don't chop the job by the time axis? We don't want different threads to write to the same result file simultaneously. Example: [Assignment 9: Parallelize NetCDF data analysis.](https://github.com/SHI200005/Comp_23/tree/main/A9_Parallel_WaveAnalysis)

#### Serial Farming

You just have a huge bunch of serial jobs (say, 3000 serial jobs). You want 10 computers to run these jobs simultaneously. When a job finished, the next job will be ran on that computer. Fortunately, you can ask for many nodes on the cluster. How to automate this process? Use **[GNU Parallel](https://www.gnu.org/software/parallel/parallel_tutorial.html)**. It solves the problem of managing blocks of subjobs of differing duration.

<img src="\images\blog\Computing_GNU.JPG" alt="Computing_GNU" style="zoom:80%;" />

Example: [Assignment 10: Managing many serial computations.](https://github.com/SHI200005/Comp_23/tree/main/A10_GNU_Serial)
