//1 以上 1,000 以下の整数を昇順で、すべて改行区切りで出力してください。

using System;

class Program
{
    static void Main()
    {
        for (int i = 0; i < 1000; i++)  //0-indexedに修正
        {
            Console.WriteLine(i + 1);
        }
    }
}