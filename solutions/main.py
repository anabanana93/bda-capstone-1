from library import download_video
from library import read_video_urls
import time

from multiprocessing import Pool
#if __name__ == "__main__":
#    url = "https://www.youtube.com/watch?v=jNQXAC9IVRw"
#    download_video(url)

if __name__ == "__main__":
    urls = read_video_urls("data/video_urls.csv")

   # start = time.perf_counter()
    
    #for url in urls:
     #download_video(url)

    #end = time.perf_counter()
    
    #elapsed = end - start

    #serial_time = round(elapsed, 2)
    #print(f"Serial execution: {serial_time}")
  
   # report = f"""# Report

    #Total time: {serial_time} seconds"""

    #with open("reports/sequential_report.md", "w") as file:
    #  file.write(report)

    serial_time = 9.78

    start = time.perf_counter()

    with Pool() as pool:
        pool.map(download_video, urls)

    end = time.perf_counter()
    parallel_time = round(end - start, 2)
    print(f"Parallel execution: {parallel_time}")


    speed_improvement = round(((serial_time - parallel_time) / serial_time) * 100, 2)

    report = f"""# Report

 ## Serial execution

 Total time: {serial_time} seconds

 ## Parallel execution

 Total time: {parallel_time} seconds

 ## Comparison

 Speed improvement: {speed_improvement}%
 """

    with open("reports/sequential_report.md", "w") as file:
        file.write(report)

    




#print(urls)