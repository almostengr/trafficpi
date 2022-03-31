namespace Almostengr.TrafficPi.Web.Services
{
    public interface IHomeService
    {
        void RebootSystem();
        void ShutDownSystem();
        void StartWorkerProcess(string programName);
        bool StopWorkerProcess();
    }
}