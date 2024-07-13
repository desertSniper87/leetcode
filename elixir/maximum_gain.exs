defmodule Solution do
  @spec maximum_gain(s :: String.t(), x :: integer, y :: integer) :: integer
  def maximum_gain(s, x, y) do
    s
    |> IO.inspect()
  end
end

Solution.maximum_gain("cdbcbbaaabab", 4, 5)
