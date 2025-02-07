#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <torch/torch.h>
#include <unordered_map>
#include <vector>
#include <random>

namespace py = pybind11;

using EdgeList = std::vector<std::tuple<int, int, float>>;
using LabelMap = std::unordered_map<int, int>;

std::vector<int> chinese_whispers(const EdgeList& edges, int num_nodes, int iterations) {
    LabelMap labels;
    std::vector<std::vector<std::pair<int, float>>> graph(num_nodes);
    
    // Inicializar el grafo
    for (const auto& [a, b, weight] : edges) {
        graph[a].emplace_back(b, weight);
        graph[b].emplace_back(a, weight);
    }
    
    // Asignar etiquetas iniciales únicas
    for (int i = 0; i < num_nodes; ++i) {
        labels[i] = i;
    }
    
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dist(0, num_nodes - 1);
    
    // Iterar para actualizar etiquetas
    for (int it = 0; it < iterations; ++it) {
        for (int i = 0; i < num_nodes; ++i) {
            int node = dist(gen);
            std::unordered_map<int, float> label_weights;
            
            for (const auto& [neighbor, weight] : graph[node]) {
                label_weights[labels[neighbor]] += weight;
            }
            
            if (!label_weights.empty()) {
                labels[node] = std::max_element(
                    label_weights.begin(), label_weights.end(),
                    [](const auto& a, const auto& b) { return a.second < b.second; })
                    ->first;
            }
        }
    }
    
    // Convertir etiquetas en un vector
    std::vector<int> result(num_nodes);
    for (const auto& [node, label] : labels) {
        result[node] = label;
    }
    return result;
}

PYBIND11_MODULE(chinese_whispers, m) {
    m.def("chinese_whispers", &chinese_whispers, "Run Chinese Whispers clustering",
          py::arg("edges"), py::arg("num_nodes"), py::arg("iterations") = 10);
}
