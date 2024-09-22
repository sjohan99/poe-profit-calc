type Drop = {
  name: string;
  price: number;
  droprate: number;
  reliable: boolean;
  trade_link: string | null;
  img: string | null;
};

type EntranceItem = {
  name: string;
  price: number;
  quantity: number;
  img: string | null;
};

export type BossInfo = {
  id: string;
  name: string;
  drops: Drop[];
  entrance_items: EntranceItem[];
};
