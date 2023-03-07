/* * * * * * * * * * * * * * * * * 
 *                               *
 *  C Pocket Card - The Basics   *
 *                               *
 *   By Yoann AMAR ASSOULINE     *
 *                               *
 * * * * * * * * * * * * * * * * */

# include <stdio.h>

// This is a Single Line Comment 

/*
	This is a
	Multi Line Comment
*/

int main (void) {

	/* * * * * * * * * * * * * * * * * * * * * * *
	 *                                           *  
	 *	Variables & Basic/ Primary Data Types    *
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
	float FloatingPointVariable = 3.25; 

	double DoubleFloatingPointVariable = 4; 

	long double LongDoubleFloatingPoint = 30945;


	return 0; 
}