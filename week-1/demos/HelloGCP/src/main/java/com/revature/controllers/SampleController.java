package com.revature.controllers;

import org.springframework.web.bind.annotation.*;

import java.util.HashSet;
import java.util.Set;

@RestController
@RequestMapping("sample")
public class SampleController {

    // Let's build a few simple methods to test our access to the application on the Google Compute Engine

    Set<String> nameSet = new HashSet<>();

    @GetMapping("test")
    public String testConnectionToVM(){
        System.out.println("Connection made to server");
        return "You've hit the server!";
    }

    @GetMapping
    public Set<String> getNameSet(){
        System.out.println("Someone requested all of the names");
        return nameSet;
    }

    @PostMapping("/{sampleName}")
    public String addNameToNameSet(@PathVariable String sampleName){
        System.out.println("The name " + sampleName + " has been added to nameSet");
        nameSet.add(sampleName);
        return "You've added " + sampleName + " to the list!";
    }

}
