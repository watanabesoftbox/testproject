import sys


def main():
    # コマンドライン引数を取得
    args = sys.argv[1:]  # 最初の要素はスクリプト名なのでスキップ
    if not args:
        print("引数が指定されていません。")
        return

    print("受け取った引数:", args)

    # 引数を処理する例
    for i, arg in enumerate(args, start=1):
        print(f"引数 {i}: {arg}")


if __name__ == "__main__":
    main()
