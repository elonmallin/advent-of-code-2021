var input = File
    .ReadAllLines("input.txt");

// oxy = "001100001101"
// co2 = "101010101110"

int Solve(string[] data)
{
    var oxy = ResolveMostOrLeastCommon(data, true);
    var co = ResolveMostOrLeastCommon(data, false);

    return oxy * co;
}

int ResolveMostOrLeastCommon(string[] data, bool mostCommon)
{
    var lineLength = data[0].Length;
    for (var i = 0; i < lineLength; i++)
    {
        var onesCount = data.Count(x => x[i] == '1');
        var half = data.Length / 2f;
        var keepChar = ((mostCommon && onesCount >= half) || (!mostCommon && onesCount < half)) ? '1' : '0';

        data = data.Where(x => x[i] == keepChar).ToArray();

        if (data.Length == 1)
        {
            break;
        }
    }

    var n = Convert.ToInt32(data[0], 2);

    return n;
}

Console.WriteLine($"Solution: {Solve(input)}");
