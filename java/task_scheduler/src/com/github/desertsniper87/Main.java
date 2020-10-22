package com.github.desertsniper87;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

class Solution {
    public int leastInterval(char[] tasks, int n) {
        String taskString = new String(tasks);


        Stream<Character> taskPipeline = taskString.chars().mapToObj(c -> (char) c);
        List<Character> taskList = taskPipeline.collect(Collectors.toList());
        Set<Character> taskSet = new HashSet<>(taskList);


        for(Character s: taskSet) {
            System.out.println(s + " " + Collections.frequency(taskList, s));
        }


        return 0;
    }
}

public class Main {

    public static void main(String[] args) {
	// write your code here
        String[] sArray = {"A","A","A","B","B","B"};
        String s = "";
        for (String n:sArray)
            s+= n;
        char[] inputArray = s.toCharArray();


        char inputStringArray[] = new char[]{};
//        String inputStringArray = Arrays.toString(new String[]{"A","A","A","B","B","B"});
//        char[] inputArray = inputStringArray.toCharArray();
        Solution solution = new Solution();
        System.out.println(solution.leastInterval(inputArray , 2));
    }
}
