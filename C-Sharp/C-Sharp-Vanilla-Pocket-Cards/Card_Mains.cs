using System;
using Card01_TheBasics; 

namespace C_Sharp_Vanilla_Pocket_Cards
{
    // Namespaces | Including other cards
    using Card01_TheBasics;
    using Card02_Functions;
    using Card03_Classes; 

    class Card00_Mains
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Card 00 Loading Screen");

            //var instance = new Card01_TheBasics.Card01_TheBasics();
            //instance.Card01_Main(); 

            Card01_TheBasics.Card01_Main(args); 

        }
    }
}