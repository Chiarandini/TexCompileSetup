
===============================================================================
		    _            _______ ________   __
		   | |        /\|__   __|  ____\ \ / /
		   | |       /  \  | |  | |__   \ V /
		   | |      / /\ \ | |  |  __|   > <
		   | |____ / ____ \| |  | |____ / . \
	     _____ |______/_/__ _\_\_|__|______/_/ \_\___ _____
	    / ____/ __ \|  \/  |  __ \_   _| |    |  ____|  __ \
	   | |   | |  | | \  / | |__) || | | |    | |__  | |__) |
	   | |   | |  | | |\/| |  ___/ | | | |    |  __| |  _  /
	   | |___| |__| | |  | | |    _| |_| |____| |____| | \ \
	    \_____\____/|_|  |_|_|   |_____|______|______|_|  \_\

==================================================================================
Setup
The point of this setup is to compile a tex file without needing to constantly
import a new preamble. I've tried to do so in a flexible way so that I could,
if I want, add packages are do some modifications

There are 4 steps in compiling a latex document
  1. Activating it in a .tex file with <leader>kk
  2. Running the vimscript that's in the .vimrc
  3. Running the .bat file which makes the file for compilation and compiles
  4. Return the files and "clean up" the non-needed files

NOTE my .vimrc code is in another repository. The function that compiles the code
is called CompileTex
==================================================================================
Special inputs

The first line of any tex file is reserved. It will contain the packages one
wants to import and special keywords such as (note that case matters):

 - letter       : Must be first in the first line. Changes document class.
		  Could also be beamer, double article, etc.
 - \[KEYWORD]   : will put in the preamble
 - no preamble  : mainly to test new packages. Must be  end of the first line.

NOTE If the first line is "\documentclass[HERE]{HERE}", then The document will be
treated as though it already has a preamble, and be compiled directly with lualatex.

==================================================================================
Different Templates

It is my goal to have different templates for different document classes. For
example, letters different specification and needs (ex. address' signatures),
and don't need things like thmtools or longtable. Thus, I will eventually create
a template suiting this purpose. The templates I want to create are:

 - Template
 - LetterTemplate
 - BeamerTemplate



==================================================================================
micro Templates

I also intented to implement micro-templates - not every file needs packages relating
to math symbols. I want to eventually create the following mini-templates:

 - microMathTemplate
 - microProgTemplate


