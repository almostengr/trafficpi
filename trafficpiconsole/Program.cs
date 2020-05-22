using System;
using System.Threading;

namespace Almostengr.TrafficPi.ConsoleControl
{
    class Program
    {
        private static bool Debug = false;

        static void Main(string[] args)
        {
#if DEBUG
            Debug = true;
#endif

            Console.WriteLine("Starting TrafficPi");
            Console.WriteLine("Press Ctrl+C to exit");
            Console.WriteLine();
        }
    }
}
