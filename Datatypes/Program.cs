namespace Datatypes
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Data Types");

            //täisnumber
            Console.WriteLine("Sisestage täisnumber.");
            string bigNumber = Console.ReadLine();
            int.Parse(bigNumber);
            Console.WriteLine("Teie täisnumber on: "+bigNumber);

            //komaga number
            Console.WriteLine("Sisestage komaga number.");
            string komaNumber = Console.ReadLine();
            double.Parse(komaNumber);
            Console.WriteLine("Teie komaga number on: "+komaNumber);

        }
    }
}
