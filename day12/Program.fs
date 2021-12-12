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


let rec traverse (me: string, links: List<string>, paths: Dictionary<string, List<string>>, disallowed: List<string>, count2: int, track: List<string>): int =
    let mutable count = count2

    for link in links do
        let trackPath = $"{me},{link}"
        if me = "start,A,b" then
            0 |> ignore
        if link = "end" then
            track.Add(trackPath)
            count <- count + 1
            0 |> ignore
        elif not (disallowed.Contains(link)) then

            let dis = new List<string>()
            for d in disallowed do
                dis.Add(d)
            if link = link.ToLower() then
                dis.Add(link)
            count <- traverse (trackPath, paths[link], paths, dis, count, track)
            0 |> ignore

    count


let solvePart1 (paths: Dictionary<string, List<string>>) =
    let disallowed = new List<string>()
    disallowed.Add("start")
    let track = new List<string>()
    let pathCount = traverse ("start", paths["start"], paths, disallowed, 0, track)
    pathCount


printfn "%i" (solvePart1 paths)


