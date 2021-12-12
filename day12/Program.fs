open System.IO
open System.Collections.Generic

let paths = new Dictionary<string, List<string>>()

for line in File.ReadAllLines("input.txt") do
    let parts = line.Split("-")

    if not (paths.ContainsKey(parts[0])) then
        paths.Add(parts[0], new List<string>())
    if parts[1] <> "start" then
        paths.Item(parts[0]).Add(parts[1])

    if not (paths.ContainsKey(parts[1])) then
        paths.Add(parts[1], new List<string>())
    if parts[0] <> "start" then
        paths.Item(parts[1]).Add(parts[0])


let rec traverse (me: string, links: List<string>, paths: Dictionary<string, List<string>>, disallowed: string list, track: List<string>, enableTwice: bool): int =
    let mutable count = 0

    for link in links do
        let trackPath = $"{me},{link}"

        if link = "end" then
            track.Add(trackPath)
            count <- count + 1
        elif not (List.contains link disallowed) then
            let dis = disallowed @ (if link = link.ToLower() then [link] else [])
            count <- count + traverse (trackPath, paths[link], paths, dis, track, enableTwice)
        elif enableTwice && not (List.contains "twice" disallowed) then
            let dis = disallowed @ ["twice"]
            count <- count + traverse (trackPath, paths[link], paths, dis, track, enableTwice)

    count


let solvePart1 (paths: Dictionary<string, List<string>>) =
    let track = new List<string>()
    let pathCount = traverse ("start", paths["start"], paths, ["start"], track, false)
    
    pathCount


let solvePart2 (paths: Dictionary<string, List<string>>) =
    let track = new List<string>()
    let pathCount = traverse ("start", paths["start"], paths, ["start"], track, true)

    pathCount


printfn "Part 1: %i" (solvePart1 paths)
printfn "Part 2: %i" (solvePart2 paths)
