using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace KalkulaatorBasic
{
    class Program
    {
        static void Main(string[] args)
        {
            double first = 0;
            double second = 0;
            
            //tervitame
            Console.WriteLine("Tere! Mina olen kalkulaator!");

            //küsime esimest numbrit
            Console.Write("Sisestage esimene number: ");
            first = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("");

            //küsime teist numbrit
            Console.Write("Sisestage teine number: ");
            second = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("");

            //küsime kas soovib liita/lahutada vms
            Console.WriteLine("Valige üks:");
            Console.WriteLine("+ : liida");
            Console.WriteLine("- : lahuta");
            Console.WriteLine("* : korruta");
            Console.WriteLine("/ : jaga");
            string valik = Console.ReadLine();
            if (valik == "+")
            {
                double vaste = first + second;
                Console.WriteLine("Vastus on: " + vaste + " !");
            }
            else if (valik == "-")
            {
                double vaste = first - second;
                Console.WriteLine("Vastus on: " + vaste + " !");
            }
            else if (valik == "*")
            {
                double vaste = first * second;
                Console.WriteLine("Vastus on: " + vaste + " !");
            }
            else if (valik == "/")
            {
                double vaste = first / second;
                Console.WriteLine("Vastus on: " + vaste + " !");
            }
        }
    }
}
