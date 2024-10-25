import curses

class Item:
    def __init__(self):
        self.items = []
        self.cancel_option = ("Cancel", self._cancel, "Cancel and exit")

    def __call__(self, func):
        # 関数の名前、関数自体、および説明をアイテムリストに追加
        description = func.__defaults__[0] if func.__defaults__ else ""
        self.items.append((func.__name__, func, description))
        return func  # デコレーターとして機能させるためにfuncを返す

    def select(self):
        return self._cli_select()

    def _cli_select(self):
        def menu(stdscr):
            curses.curs_set(0)
            selected_index = 0
            search_query = ""
            all_items = self.items + [self.cancel_option]

            while True:
                stdscr.clear()
                height, width = stdscr.getmaxyx()

                # 検索バーの表示
                search_prompt = "Search: " + search_query
                stdscr.addstr(0, 0, search_prompt, curses.A_UNDERLINE)

                # フィルタリングされたアイテムの取得
                filtered_items = self._filter_items(search_query, all_items)

                # 表示するアイテムの調整（最大表示可能行数に基づく）
                display_items = filtered_items[:height - 2]  # 検索バーと余白を考慮
                for idx, (name, _, description) in enumerate(display_items):
                    if idx == selected_index:
                        stdscr.addstr(idx + 1, 0, f"> {name}: {description}", curses.A_BOLD)
                    else:
                        stdscr.addstr(idx + 1, 0, f"  {name}: {description}")

                key = stdscr.getch()

                if key in (curses.KEY_UP, ord('k')):
                    selected_index = (selected_index - 1) % len(display_items) if display_items else 0
                elif key in (curses.KEY_DOWN, ord('j')):
                    selected_index = (selected_index + 1) % len(display_items) if display_items else 0
                elif key in (curses.KEY_BACKSPACE, 127, 8):
                    search_query = search_query[:-1]
                    selected_index = 0
                elif key in [curses.KEY_ENTER, ord("\n")]:
                    if display_items:
                        return display_items[selected_index]
                elif key == 27:  # ESCキーでキャンセル
                    return self.cancel_option
                elif 32 <= key <= 126:  # Printable characters
                    search_query += chr(key)
                    selected_index = 0

                stdscr.refresh()

        return curses.wrapper(menu)

    def _filter_items(self, query, items):
        if not query:
            return items
        query_lower = query.lower()
        return [item for item in items if query_lower in item[0].lower() or query_lower in item[2].lower()]

    def _cancel(self):
        # キャンセル時の処理（必要に応じて拡張可能）
        pass

    def endwin(self):
        curses.endwin()

item = Item()

def main():
    # Placeholder for console script entry point
    pass

if __name__ == '__main__':
    main()
