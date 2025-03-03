namespace ForLoop_2_KillKoll
{
    internal class Program
    {
        static void Main(string[] args)
        {           
            for (int y = 0; y < 3; y++)
            {
                for (int i = 0; i < 2; i++)
                {
                    Console.WriteLine("kill-koll");
                    if (i == 1)
                    {
                        for (int j = 0; j < 1; j++)
                        {
                            Console.WriteLine("killadi-koll");
                        }
                    }
                }
            }
        }
    }
}
