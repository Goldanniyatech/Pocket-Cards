using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Card01_TheBasics
{
    public class Card01_TheBasics
    {
        public static void Card01_Main (string[] args)
        {
            Console.WriteLine("Card 01: The Basics Loaded"); 
        }

        /* * * * * * * * * * * * * * * * * * * * * *
         *                                         *
         *          Variables & Data Types         *
         *               (Theory)                  *
         *                                         *
         * * * * * * * * * * * * * * * * * * * * * */


        // Variable Naming Convention: PascalCase (Other convention: snake_case, camelCase, kebab-case)
        // There are 3 types of data Types: Value, Reference and Pointers

        // Value Data Types (predefined & user-defined)

        // Integer Data Type
        int IntegerVariable = 53045;

        // Floating-Point Data Type 
        float FloatingPointVariable = 3405.5F;
        double DoubleVariable = 0.0D;
        decimal DecimalVariable = 0.0M;

        // Boolean Data Type
        bool BooleanVariable = true;

        // Character Data Type 
        char CharacterVariable = 'A';

        // String Data Type 
        string StringVariable = "Hello World \n";
        string VerbatimStringVariable = @"Hello \n"; // A verbatim string literal ignore escape sequences, hexadecimal escape sequences and Unicode escape sequences. The "quote" isn't ignore, though


		// Variables & Data Types (Real-Life Examples)

		int CharacterLife = 100;


        float VehicleSpeed = 0.0F;
        float VehicleSpeedMax = 150.0F;

    }
}
