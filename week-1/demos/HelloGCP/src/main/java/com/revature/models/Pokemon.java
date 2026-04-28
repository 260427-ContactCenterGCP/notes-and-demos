package com.revature.models;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

import java.util.Objects;

// Entity makes sure this is tracked by JPA
@Entity
// Table allows us to provide table config info
@Table(name = "pokemon")
public class Pokemon {

    // Marks column as primary key
    @Id
    private int pokemonId;

    private String name;

    // Provides column config info
    @Column(nullable = false)
    private String type1;

    private String type2;

    public int getPokemonId() {
        return pokemonId;
    }

    public void setPokemonId(int pokemonId) {
        this.pokemonId = pokemonId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getType1() {
        return type1;
    }

    public void setType1(String type1) {
        this.type1 = type1;
    }

    public String getType2() {
        return type2;
    }

    public void setType2(String type2) {
        this.type2 = type2;
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        Pokemon pokemon = (Pokemon) o;
        return pokemonId == pokemon.pokemonId && Objects.equals(name, pokemon.name) && Objects.equals(type1, pokemon.type1) && Objects.equals(type2, pokemon.type2);
    }

    @Override
    public int hashCode() {
        return Objects.hash(pokemonId, name, type1, type2);
    }

    @Override
    public String toString() {
        return "Pokemon{" +
                "pokemonId=" + pokemonId +
                ", name='" + name + '\'' +
                ", type1='" + type1 + '\'' +
                ", type2='" + type2 + '\'' +
                '}';
    }
}
