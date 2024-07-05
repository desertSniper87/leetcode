defmodule Solution do
  @spec longest_common_prefix(strs :: [String.t()]) :: String.t()
  def longest_common_prefix([]), do: ""
  def longest_common_prefix([single_str]), do: single_str

  def longest_common_prefix([first | rest]) do
    Enum.reduce(rest, first, fn str, acc ->
      common_prefix(acc, str)
    end)
  end

  defp common_prefix(str1, str2) do
    Enum.zip(String.graphemes(str1), String.graphemes(str2))
    |> Enum.take_while(fn {char1, char2} -> char1 == char2 end)
    |> Enum.map(&elem(&1, 0))
    |> Enum.join("")
  end
end
