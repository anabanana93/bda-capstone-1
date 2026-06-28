from library import download_video
from library import read_video_urls
import time

from multiprocessing import Pool
#if __name__ == "__main__":
#    url = "https://www.youtube.com/watch?v=jNQXAC9IVRw"
#    download_video(url)
import csv
from library import  get_video_metadata


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
    results = []
    for url in urls:
        result = download_video(url)
        results.append(result)
    succesful_downloads = sum (1 for r in results if r ["status"]=="success")
    failed_downloads = sum (1 for r in results if r ["status"]=="failed")


   # with Pool() as pool:
        #pool.map(download_video, urls)

    metadata_rows = []
    for url in urls:
        metadata = get_video_metadata(url)
        metadata_rows.append(metadata)

    end = time.perf_counter()
    parallel_time = round(end - start, 2)
    print(f"Parallel execution: {parallel_time}")


    fieldnames = ["title", "duration", "uploader", "view_count", "ext", "url"]
    with open("data/video_metadata.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(metadata_rows)

    speed_improvement = round(((serial_time - parallel_time) / serial_time) * 100, 2)

    report = f"""# Report

 ## Serial execution

 Total time: {serial_time} seconds

 ## Parallel execution

 Total time: {parallel_time} seconds

 ## Comparison

 Speed improvement: {speed_improvement}%
 ## Download status

Successful downloads: {succesful_downloads}
Failed downloads: {failed_downloads} 
 """

    with open("reports/sequential_report.md", "w") as file:
        file.write(report)


    for result in results:
        if result["status"] == "failed":
            print("Failed:", result["url"])
            print("Error:", result["error"])

#print(urls)


#print(urls)