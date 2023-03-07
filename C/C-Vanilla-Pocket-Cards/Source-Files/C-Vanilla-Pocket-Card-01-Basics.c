/* * * * * * * * * * * * * * * * * 
 *                               *
 *  C Pocket Card - The Basics   *
 *                               *
 *   By Yoann AMAR ASSOULINE     *
 *                               *
 * * * * * * * * * * * * * * * * */

// Header Files
# include <stdio.h>

// C99 Header Files
#include <stdbool.h>

// This is a Single Line Comment 

/*
	This is a
	Multi Line Comment
*/

int main (void) {

	/* * * * * * * * * * * * * * * * * * * * * * *
	 *                                           *  
	 *	Variables & Basic/ Primary Data Types    *
	 *				   Theory                    *
	 *                                           *
	 * * * * * * * * * * * * * * * * * * * * * * */
	// Variable Naming Convention Used here: PascalCase (other existing conventions: snake_case, camelCase, kebab-case)
	

	// Basic Data Types comes in two flavors: signed and unsigned 
	// Those are called Type Modifiers. Signed allows both positive & negative numbers, while unsigned store only positive numbers. 
	// Outside of char, each data type is signed by default. 
	// However, most of the time, those are signed by default


	// Character variables
	char CharacterVariable = 'a'; 
	unsigned CharacterVariableUnsigned = 'b'; 
	signed CharacterVariableSigned = 'c'; 



	// Integer Variables
	int IntegerVariable = 150;
	signed int IntegerVariableSigned = -48545;
	unsigned int IntegerVariableUnsigned = 455; 

	short ShortVariable = 120; 
	signed ShortVariableSigned = 54541; 
	unsigned short ShortVariableUnsigned = 455; 

	long LongVariable = 93445; 
	signed long LongVariableSigned = 3540; 
	unsigned long LongVariableUnsigned = 395; 


	// Floating-Point Variables 
	// Note that we don't have unsigned support, since there is no equivalent machine code operation. 
	float FloatingPointVariable = 3.25; 

	double DoubleFloatingPointVariable = 4; 

	long double LongDoubleFloatingPoint = 30945;


	// Booleans 

	/*  Booleans: Method 1 (The Old Way)
		Before C99, we had to either use signed int (where 0 means false and 1 means true) 
		or explicitely define a boolean type */

	#define custom_bool unsigned int
	#define custom_false 0
	#define custom_true 1 

	signed int IntegerBoolean = 1; // True
	custom_bool CustomBoolean = custom_true; // Equivalent to 1 

	/*	Boolean: Method 2 (After C99)  
		A native way to use booleans was with the "_Bool" reserved keyword, which has an underscore (and uppercase) to avoid
		any compatibility issue with existing projects. 

		However, for projects who never use the "bool" keyword, they can use <stdbool.h> and, thus, use the "bool" keyword.
	*/ 

	_Bool BooleanVariableC99 = 1; // Native way of supporting boolean in C99 
	bool BooleanVariableC99STD = true; // "bool" keyword support only when <stdbool.h> is included. 
	 
	/* * * * * * * * * * * * * * * * * * * * * * *
	 *                                           *
	 *	Variables & Basic/ Primary Data Types    *
	 *			  Real-life Examples             *
	 *                                           *
	 * * * * * * * * * * * * * * * * * * * * * * */

	char StudentGrade = 'A'; 
	printf (" Student Grade:  %c \n", StudentGrade); 

	int RoomTemperature = -10; 
	float CharacterSpeed = 45.34; 




	/* * * * * * * * * * * * * * * * * * * * * * * * *
	 *                                               *
	 *	Variables & Derived/ Secondary Data Types    *
	 *				   Theory                        *
	 *                                               *
	 * * * * * * * * * * * * * * * * * * * * * * * * */




	 /* * * * * * * * * * * * * * * * * * * * * * * * *
	  *                                               *
	  *             	Conditions                    *
	  *				   Theory                         *
	  *                                               *
	  * * * * * * * * * * * * * * * * * * * * * * * * */

	if (RoomTemperature < 0)
	{
		printf("It's really cold here! Let's move!");
	}
	else if (RoomTemperature > 10)
	{
		printf("We can stay a little longer!");
	}
	else
	{
		printf("We better go! NOW!");
	}



	return 0; 
}