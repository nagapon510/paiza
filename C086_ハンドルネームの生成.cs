/*インターネットのとあるサービスで利用するためのハンドルネームを作ることにしました。
そのハンドルネームは名前の文字列から母音を取り除いて子音のみを連結して生成します。

ただし、ここで母音とは "a", "e", "i", "o", "u" の 5 つのアルファベットの小文字( "a", "e", "i", "o", "u" )、
大文字( "A", "E", "I", "O", "U" )を指し、子音とはそれ以外のアルファベットを意味します。*/

using System;
using System.Linq;

class Program
{
    static void Main()
    {
        var name = Console.ReadLine();

        //入力値がnullだったらそのまま処理終了（早期リターン）
        if (name == null) return;

        //nameを1文字単位で分割して配列に代入⇒whereで子音を抽出⇒ToListで配列を子音に変換
        var ret = name.ToCharArray().Where(x => x != 'a' && x != 'i' && x != 'u' && x != 'e' && x != 'o').ToList();

        //区切り文字なしでリストの文字列を結合
        Console.WriteLine(String.Join("",ret));
    }
}