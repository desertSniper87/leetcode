    def reverseVowels(self, s: str) -> str:
      vowel_position = []
      for i in range(len(s)):
        if s[i] in 'aeiouAEIOU':
          vowel_position.append(i)

      list_s = list(s)

      for i in range(len(vowel_position)):
        list_s[vowel_position[i]] = s[vowel_position[-i-1]]
        list_s[vowel_position[-i-1]] = s[vowel_position[i]]
      return ''.join(x for x in list_s)
