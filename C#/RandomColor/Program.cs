namespace RandomColor
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Random Color");

            for (int i = 0; i < 130; i++)
            {
                Colour c = (Colour)(new Random()).Next(0, 5);
                switch (c)
                {
                    case Colour.Red:
                        Console.BackgroundColor = ConsoleColor.Red;
                        Console.Clear();
                        Console.WriteLine("Red");
                        break;
                    case Colour.Green:
                        Console.BackgroundColor = ConsoleColor.Green;
                        Console.Clear();
                        Console.WriteLine("Green");
                        break;
                    case Colour.Blue:
                        Console.BackgroundColor = ConsoleColor.Blue;
                        Console.Clear();
                        Console.WriteLine("Blue");
                        break;
                    case Colour.Yellow:
                        Console.BackgroundColor = ConsoleColor.Yellow;
                        Console.Clear();
                        Console.WriteLine("Yellow");
                        break;
                    case Colour.Gray:
                        Console.BackgroundColor = ConsoleColor.Gray;
                        Console.Clear();
                        Console.WriteLine("Gray");
                        break;
                    case Colour.White:
                        Console.BackgroundColor = ConsoleColor.White;
                        Console.Clear();
                        Console.WriteLine("White");
                        break;
                    default:
                        Console.WriteLine("Err");
                        break;
                }
            }
            Colour colour = (Colour)(new Random()).Next(0, 5);
            Console.WriteLine("The color is {0}", colour);
        }
    }
    public enum Colour
    {
        Red, Green, Blue, Yellow, Gray, White
    }
}   
