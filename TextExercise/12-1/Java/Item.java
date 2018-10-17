/**
 * 貪欲アルゴリズムの品物に関するJava実装
 */
public class Item implements HasWeightAndValue{
    private String name;
    private int value;
    private float weight;

    /**
     * コンストラクタ。Immutable Objectにするのでここでしか値はセットされない。
     * @param name 名称
     * @param value 価値
     * @param weight 重さ
     */
    public Item(String name, int value, int weight) {
        this.name = name;
        this.value = value;
        this.weight = weight;
    }

    /**
     * 名称を取得する。
     * @return 名称
     */
    public String getName() {
        return this.name;
    }

    /**
     * 価値を取得する。
     * @return 価値
     */
    @Override
    public float getValue() {
        return (float)this.value;
    }

    /**
     * 質量を取得する。
     * @return 質量
     */
    @Override
    public float getWeight() {
        return (float)this.weight;
    }    
}