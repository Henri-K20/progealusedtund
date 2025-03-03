namespace StringIfAndElse
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.ForegroundColor = ConsoleColor.Yellow;

            Console.WriteLine("Mis on teie nimi?");
            Console.ForegroundColor = ConsoleColor.White;

            string nimi = Console.ReadLine();
            if (string.IsNullOrEmpty(nimi) == true)
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Err. See ei ole nimi.");
                Console.Beep();
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine("Sinu nimi on " + nimi);
            }
        }
    }
}
