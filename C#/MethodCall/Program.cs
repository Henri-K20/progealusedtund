namespace MethodCall
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //meetodite tegemine sama, kui pythonis funktsiooni definimine
            //C# kasutab static void
            //python kasutab lihtsalt def


            Console.WriteLine("Hello, World!");
            //calling jalgratas
            Jalgratas();
        }
        static void Jalgratas()
        {
            Console.WriteLine("Nüüd oled jalgratta meetodis");
        }
    }
}
