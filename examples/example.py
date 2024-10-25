from jobflow import run_locally
from itemlist import item

if __name__ == '__main__':
    from main_flow import flow, flow2, flow3

    @item
    def flow_runner(description="Run the first flow"):
        run_locally(flow)

    @item
    def flow2_runner(description="Run the second flow"):
        run_locally(flow2)

    @item
    def flow3_runner(description="Run the third flow"):
        run_locally(flow3)

    selected = item.select()
    item.endwin()

    selected_name, selected_func, selected_func_description = selected

    if selected_func == item._cancel:
        print("キャンセルが選択されました。プログラムを終了します。")
    else:
        print(f"Running: {selected_name}\n")
        print(f"Description: {selected_func_description}\n")
        selected_func()
