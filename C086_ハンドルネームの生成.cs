/*インターネットのとあるサービスで利用するためのハンドルネームを作ることにしました。
そのハンドルネームは名前の文字列から母音を取り除いて子音のみを連結して生成します。

ただし、ここで母音とは "a", "e", "i", "o", "u" の 5 つのアルファベットの小文字( "a", "e", "i", "o", "u" )、
大文字( "A", "E", "I", "O", "U" )を指し、子音とはそれ以外のアルファベットを意味します。*/

using System;
using System.Text;

class Program
{
    static void Main()
    {
        var name = Console.ReadLine();
        char[] charName = name.ToCharArray();
        StringBuilder handleName = new StringBuilder();  //初期化時の空文字の除外
        for (int i = 0; i < charName.Length; i++)
        {
            if (charName[i] == 'a' || charName[i] == 'i' || charName[i] == 'u' || charName[i] == 'e' || charName[i] == 'o')
            {
                continue;  //条件を満たす場合は何も処理をせずに返す。
            }
            handleName.Append(charName[i]);   //今回の場合elseでの分岐は不要。
        }
        Console.WriteLine(handleName);
    }
}