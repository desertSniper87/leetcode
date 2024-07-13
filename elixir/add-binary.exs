defmodule Solution do
  @spec add_binary(a :: String.t(), b :: String.t()) :: String.t()
  def add_binary(a, b) do
    to_decimal = fn x -> Integer.parse(x, 2) end
    to_binary = fn x -> Integer.to_string(x, 2) end

    Enum.map([a, b], to_decimal)
    |> Enum.map(&elem(&1, 0))
    |> Enum.sum()
    |> to_binary.()
  end
end

IO.inspect(Solution.add_binary("11", "1"))
