using System;
using System.Device.Gpio;
using System.Threading;

namespace Almostengr.TrafficPi
{
    public class MockControl : ITrafficControl
    {
        public void RunControl()
        {
            while (true)
            {
                Console.WriteLine("===== Main Menu =====");
                Console.WriteLine();
                Console.WriteLine("0 = Off");
                Console.WriteLine("1 = Red");
                Console.WriteLine("2 = Yellow");
                Console.WriteLine("3 = Green");
                
                Console.WriteLine();
                Console.Write("Enter selection: ");

                string input = Console.ReadLine();

                switch (input)
                {
                    case "0":
                        Console.WriteLine("Off");
                        break;

                    case "1":
                        Console.WriteLine("red");
                        break;

                    case "2":
                        Console.WriteLine("yellow");
                        break;

                    case "3":
                        Console.WriteLine("green");
                        break;

                    default:
                        Console.WriteLine("Invalid selection");
                        break;
                }
                
                Console.WriteLine();
            }
        }
    }
}