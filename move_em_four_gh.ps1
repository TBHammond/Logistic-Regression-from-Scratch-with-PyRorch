$file_list = Get-Content D:\training_files_flooding.txt
$search_folder = "D:\data\training_png"
$destination_folder = "D:\data\train\flooding"

foreach ($file in $file_list) {
    $file_to_move = Get-ChildItem -Path $search_folder -Filter $file #-Recurse -ErrorAction SilentlyContinue -Force | % { $_.FullName}
    if ($file_to_move) {
        Move-Item $file_to_move $destination_folder
    }
}