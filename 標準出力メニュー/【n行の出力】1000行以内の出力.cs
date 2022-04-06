//数値 N が入力されます。1 から N までの数値をすべて、改行区切りで出力してください。

using System;

class Program
{
    static void Main()
    {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        var number = int.Parse(Console.ReadLine());
        for (int i = 0; i + 1 <= number; i++)
        {
            Console.WriteLine(i + 1);
        }
    }
}