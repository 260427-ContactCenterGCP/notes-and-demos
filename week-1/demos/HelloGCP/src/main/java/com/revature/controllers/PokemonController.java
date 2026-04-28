package com.revature.controllers;

import com.revature.dao.PokemonDAO;
import com.revature.models.Pokemon;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("pokemon")
public class PokemonController {

    private final PokemonDAO pokemonDAO;

    @Autowired
    public PokemonController(PokemonDAO pokemonDAO) {
        this.pokemonDAO = pokemonDAO;
    }

    @GetMapping
    public List<Pokemon> getAllPokemon(){
        return pokemonDAO.findAll();
    }

    @GetMapping("/{type1}")
    public List<Pokemon> getAllPokemonByType1(@PathVariable String type1){
        return pokemonDAO.getPokemonByType1(type1);
    }

    @PostMapping
    public Pokemon addPokemon(@RequestBody Pokemon p){
        return pokemonDAO.save(p);
    }
}
