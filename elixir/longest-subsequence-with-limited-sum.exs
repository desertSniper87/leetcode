defmodule Solution do
  @spec answer_queries(nums :: [integer], queries :: [integer]) :: [integer]
  def answer_queries(nums, queries) do
    prefix_sum =
      nums
      |> Enum.sort()
      |> Enum.scan(fn x, y -> x + y end)

    queries
    |> Enum.map(&get_longest_subseq(&1, prefix_sum))
  end

  defp get_longest_subseq(target, prefix_sum) do
    prefix_sum
    |> Enum.filter(fn x -> x <= target end)
    |> length()
  end
end

nums = [4, 5, 2, 1]
queries = [3, 10, 21]

IO.inspect(Solution.answer_queries(nums, queries))

nums = [2, 3, 4, 5]
queries = [1]

IO.inspect(Solution.answer_queries(nums, queries))
