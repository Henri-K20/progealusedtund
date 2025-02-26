using System.Runtime.InteropServices;

namespace rectangelCalc
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //tervitus
            Console.WriteLine("Tere! Mina olen ristküliku kalkulaator!");

            // küsime esimest numbrit
            Console.WriteLine("Enter first value");
            string firstNumber = Console.ReadLine();
            float floatFirst = float.Parse(firstNumber);

            //küsime teist numbrit
            Console.WriteLine("Enter second value");
            string secondNumber = Console.ReadLine();
            float floatSecond = float.Parse(secondNumber);

            // pindala kalkulatsioon
            float pindala = floatFirst * floatSecond;
            Console.WriteLine("Pindala on " + pindala);

            //ümbermõõdu kalkulatsioon
            float ümbermõõt = 2 * (floatFirst + floatSecond);
            Console.WriteLine("Ümbermõõt on " + ümbermõõt);



            // tervitus ruut
            Console.WriteLine("Tere! Mina olen ruudu kalkulaator!");

            //küsime esimest numbrit
            Console.WriteLine("Kirjutage ruudu ühe külje pikkus");
            string külgruut = Console.ReadLine();
            float floatkülgruut = float.Parse(külgruut);

            //ruudu pindala
            float ruutpindala = floatkülgruut * floatkülgruut;
            Console.WriteLine("Ruudu pindala on " + ruutpindala);

            //ruudu ümbermõõt
            float ruuduümbermõõt = floatkülgruut * 4;
            Console.WriteLine("Ruudu ümbermõõt on " + ruuduümbermõõt);


            //tervitus kolmnurk
            Console.WriteLine("Tere! Mina olen täisnurkse kolmnurga kalkulaator!");

            //küsin pikeima külje pikkust
            Console.WriteLine("Sisestage pikeima külje pikkus");
            string kolmPikeim = Console.ReadLine();
            float floatkolmPikeim = float.Parse(kolmPikeim);
            //küsin kaatetite külje pikkust
            Console.WriteLine("Sisestage kaatetite külje pikkused");
            string kolmEsimene = Console.ReadLine();
            string kolmTeine = Console.ReadLine();
            float floatkolmEsimene = float.Parse(kolmEsimene);
            float floatkolmTeine = float.Parse(kolmTeine);

            //kolmnurga pindala
            float kolmpind = (floatkolmEsimene * floatkolmTeine) / 2;
            Console.WriteLine("Kolmnurga pindala on " + kolmpind);

            //kolmnurga ümbermõõt
            float kolmümber = floatkolmPikeim + floatkolmEsimene + floatkolmTeine;
            Console.WriteLine("Kolmnurga ümbermõõt on " + kolmümber);

            //ringi calc
            Console.WriteLine("Tere! Mina olen ringi kalkulaator!");

            //küsime raadiust
            Console.WriteLine("Sisestage ringi raadius");
            string raadius = Console.ReadLine();
            float floatraadius = float.Parse(raadius);

            //ringi pindala
            double ringpindala = 3.14159 * (floatraadius * floatraadius);
            Console.WriteLine("Ringi pindala on " + ringpindala);

            //ringi ümbermõõt
            double ringümber = 2 * 3.14159 * floatraadius;
            Console.WriteLine("Ringi ümbermõõt on " + ringümber);


        }
    }
}
