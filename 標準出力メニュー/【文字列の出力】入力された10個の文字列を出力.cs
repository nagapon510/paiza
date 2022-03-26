//10 個の文字列 S_1, S_2, S_3, ..., S_10 が半角スペース区切りで与えられます。
//これらの文字列をすべて、改行区切りで出力してください。

using System;

class Program
{
    static void Main()
    {
        var line = Console.ReadLine();
        string[] strs = line.Split(' ');
        foreach (var str in strs)
        {
            Console.WriteLine(str);
        }
    }
}