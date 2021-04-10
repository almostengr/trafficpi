using System;

namespace Almostengr.TrafficPi.Signal.Utilites
{
    public static class GetDelay
    {

        public static int RandomDelay(int color)
        {
            Random random = new Random();
            int min, max;

            switch (color)
            {
                case 11:
                case 10:
                    min = 5;
                    max = 60;
                    break;
                case 9:
                    min = 2;
                    max = 5;
                    break;
                default:
                    min = 5;
                    max = 10;
                    break;
            }

            return random.Next(min, max) * 1000;
        }
    }
}