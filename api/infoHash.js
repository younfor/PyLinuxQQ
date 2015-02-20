function(x, K) {
            for (var N = K + "password error", T = "", V = []; ; )
                if (T.length <= N.length) {
                    T += x;
                    if (T.length == N.length)
                        break
                } else {
                    T = T.slice(0, N.length);
                    break
                }
            for (var U = 0; U < T.length; U++)
                V[U] = T.charCodeAt(U) ^ N.charCodeAt(U);
            N = ["0", "1", "2", "3", 
                "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"];
            T = "";
            for (U = 0; U < V.length; U++) {
                T += N[V[U] >> 4 & 15];
                T += N[V[U] & 15]
            }
            return T
        }