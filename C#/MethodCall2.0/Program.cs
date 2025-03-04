namespace MethodCall2._0
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Sisestage arv!");
            int arv = int.Parse(Console.ReadLine());

            if (arv % 2 == 0)
            {
                paaris();
            }
            else if (arv % 2 != 0)
            {
                paaritu();
            }
        }
        static void paaris()
        {           
            Console.WriteLine("See on paaris arv!");
        }
        static void paaritu()
        {
            Console.WriteLine("See on paaritu arv!");
        }
    }
}
