namespace IfAndElse
{
    internal class Program
    {
        static void Main(string[] args)
        {
            while (true)
            {
                Console.ForegroundColor = ConsoleColor.White;
                Console.WriteLine("Tere! Kui vana olete?");
                string vanus = Console.ReadLine();

                if (int.TryParse(vanus, out int value))
                {
                    int ivanus = int.Parse(vanus);
                    if (ivanus < 18)
                    {
                        Console.ForegroundColor = ConsoleColor.Cyan;
                        Console.WriteLine("Olete alaealine!");
                        break;
                    }
                    else if (ivanus >= 18 && ivanus <= 65)
                    {
                        Console.ForegroundColor = ConsoleColor.Green;
                        Console.WriteLine("Olete täisealine!");
                        break;
                    }
                    else if (ivanus > 65)
                    {
                        Console.ForegroundColor = ConsoleColor.Yellow;
                        Console.WriteLine("Olete pensionäär.");
                        break;
                    }
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Err. Väär sisestus.");
                    Console.WriteLine("Proovige uuesti!");
                }
            }
        }
    }
}
